from website_analysis.class_interface import *
from website_analysis.common_words import *

class WebPageAnalysisChart(IWebPageAnalysisChart,CommonWords):
    '''implements the IWebPageAnalysis interface class methods and finds the most common word used in the site, shows them in a pie and bar chart methods'''
    
    def bar_chart(self):
        '''this method plots bar chart and returns the ploted chart'''
        
        x_axis = np.array(self.words_found())
        y_axis = np.array(self.total_words_found())
        return plt.bar(x_axis,y_axis)
        
    
    def pie_chart(self):
        '''this method plots pie chart and returns the ploted chart'''
        y_axis = np.array(self.total_words_found())
        return plt.pie(y_axis, labels = self.words_found(), autopct = '%1.2f%%', shadow = True)
        

    
    def display_charts(self):
        '''this method diplays the ploted pie and bar charts on the same modal and also diplays the most used word'''
        print(f'The top word is: {self.words_found()[0]}')
        plt.subplot(1, 2, 1)
        plt.title(f'Website Anlaysis(The top word is: {self.words_found()[0]})')  
        plt.xlabel('Most Common Words (Top 7)')  
        plt.ylabel('Number of Times Used') 
        self.bar_chart()
        plt.subplot(1, 2, 2)
        self.pie_chart()
        plt.show()