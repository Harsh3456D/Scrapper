import PyScrappy

def imgscrape() -> str:
    valuelist: list = []
    number:int = int(input('Enter the number of images -> '))
    
    while True:
        value:str = str(input('Enter the Image Data to scrape -> '))
        valuelist.append(value.capitalize + 'Plant')
        
        choice:str = str(input("Do you want to append more (N to stop) -> "))
        
        if choice.lower() == 'n':
            break
        
    
    for values in valuelist:
        obj = PyScrappy.image_scrapper(data_name=values, img_format='jpg', n_images=number , folder_name=values)

if __name__ == '__ScrapperV2__':
    imgscrape()