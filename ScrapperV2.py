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

# ( Chrome webkit issue )
# class stockscrape:
#     def __init__(self, Stkcode):
#         self.Stkcode = Stkcode
    
#     def analysisData(self) -> any:
#         obj = PyScrappy.StockScrapper().analysis_data_scrapper(stock_code=self.Stkcode, analysis_type='growth estimate')
#         df = pd.DataFrame(obj)
#         df.to_csv(f'csvFiles\\analysis-{self.Stkcode}.csv', index=True)
#         print("Done")
        
#     def historicalData(self) -> any:
#         obj = PyScrappy.StockScrapper().historical_data_scrapper(stock_code=self.Stkcode, time_period=max, frequency='weekly')
#         df = pd.DataFrame(obj)
#         df.to_csv(f'csvFiles\\historical-{self.Stkcode}.csv', index=True)
#         print("Done")
        
#     def profileData(self) -> any:
#         obj = PyScrappy.StockScrapper().profile_data_scrapper(stock_code=self.Stkcode)
#         df = pd.DataFrame(obj)
#         df.to_csv(f'csvFiles\\profile-{self.Stkcode}.csv', index=True)
#         print("Done")

# stkcode = 'BTC'
# stockscrape(stkcode).analysisData()


if __name__ == '__ScrapperV2__':

    imgscrape()
