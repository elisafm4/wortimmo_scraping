def search_by(transaction_type, location, property_type, radius = 0, price_min = '', price_max = '',min_beds = '',max_beds = '',surface_min = '', surface_max = ''):
    '''
        Function for setting the filters applied. It gives the url to access the data
        * Inputs:
            - transaction_type: values accepted 'vente' for buying or 'location' for rent
            - location: country, city or region. Codes in readme file
            - property_type: appartment, duplex, farm... Codes in readme file
            - radius: to extend the search by location
            - price_min: min price wanted
            - price_max: max price wanted
            - min_beds: min number of beds
            - max_beds: max number of beds
            - surface_min: min surface in m2
            - surface_max: max surface in m2
        * Outputs:
            - wortimmo:url to search
    '''
   
    # check if a place for rent or buy
    if transaction_type == 'vente':
        trans = 'purchase'
    elif transaction_type == 'location':
        trans = 'rent'
        
    wortimmo = str("https://www.wortimmo.lu/en/search?property_search_engine%5BtransactionType%5D="+transaction_type
    +"&property_search_engine%5Blocation%5D="+location
    +"&property_search_engine%5Bradius%5D="+str(radius)
    +"&property_search_engine%5BpropertyTypes%5D%5B%5D="+str(property_type)
    +"&property_search_engine%5B"+trans+"PriceMin%5D="+str(price_min)
    +"&property_search_engine%5B"+trans+"PriceMax%5D="+str(price_max)
    +"&property_search_engine%5BbedroomMin%5D="+str(min_beds)
    +"&property_search_engine%5BbedroomMax%5D="+str(max_beds)
    +"&property_search_engine%5BsurfaceMin%5D="+str(surface_min)
    +"&property_search_engine%5BsurfaceMax%5D="+str(surface_max)
    +"&property_search_engine%5Bsubmit%5D=&sort_by=newest_date")
    return wortimmo
    

def get_data(html_page,num = 0):
    '''
        Function for getting the dataset. 
        * Inputs:
            - html_page: html doc with the data of the page
            - num: (optional) numbers of adverts to include in the dataset
        * Outputs:
            - wortimmo_df: dataframe with the information
                · {description, price, area, num. rooms, num. parkings, zone, agency, contact, url}
    '''
    
    # setting up the lists that will form our dataframe with all the results
    descriptions = []
    prices = []
    areas = []
    places = []
    rooms = []
    parkings = []
    agencies = []
    tlfs = []
    urls = []

    house_containers = html_page.find_all('div', class_="c-organism c-property-result-block")

    if house_containers != []:
        # check if want to determine number of adverts to show
        if num == 0:
            num = len(house_containers)
        for container in house_containers[0:num]: 
            # Description
            description = container.find_all(class_="c-title")[0].text
            description = description.replace("\n    ","")
            descriptions.append(description)

            # Price          
            price = container.find_all('div', class_="c-price c-text c-text__price")[0].text
            price = price.replace("\n    ","")
            price = price.replace("\n","")
            currency = price[-1]
            price = float(price.replace(" ","")[:-1])
            prices.append(price)

            # Area
            area = container.find_all('span')[4].text
            area = area.replace("\n                ","")
            area = area.replace("\n            ","")
            measure = area[-2:]
            area = "".join(itertools.takewhile(str.isdigit, area))
            areas.append(area)            

            # Rooms
            num_hab = container.find_all('span')[5].text   
            num_hab = num_hab.replace("\n                ","")
            num_hab = "".join(itertools.takewhile(str.isdigit, num_hab))
            rooms.append(num_hab)

            # place
            place = description.split("in",1)[1]
            places.append(place)

            # Parking
            num_parking = container.find_all('span')[6].text
            num_parking = num_parking.replace("\n                ","")
            num_parking = num_parking.replace("\n        ","")
            if num_parking == '-':
                num_parking = 0
            parkings.append(int(num_parking))
            
            # Agency
            agency = container.find_all(class_="agency")[0]
            agency = agency.a['title']
            if not agency or agency == None:
                agency = '-'            
            agencies.append(agency)
            
            # Tlf
            tlf = container.find_all('a', class_='c-button c-button__outlined')[0].get('href')
            if not tlf or tlf == None:
                tlf = '-' 
            tlfs.append(tlf)
         
            # url
            link = 'https://www.wortimmo.lu' + container.find_all('a')[0].get('href')
            urls.append(link)
            
        # Create dataframe
        cols = ['Description', str('Price ('+currency+')'), str('Area ('+measure+')'), 'Num. Rooms', 'Zone', 'Num. Parkings', 'Agency', 'URL', 'Contact']

        wortimmo_df = pd.DataFrame({'Description': descriptions,
                                    str('Price ('+currency+')'): price,
                                    str('Area ('+measure+')'): areas,
                                    'Num. Rooms': rooms,
                                    'Num. Parkings': parkings,
                                    'Zone': places,
                                    'Agency': agencies,
                                    'Contact': tlfs
                                    'URL': urls,
                                  })[cols]
        return wortimmo_df
        print ('Dataframe created')
    else:
        return"No results found"   
