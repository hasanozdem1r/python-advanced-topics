import wikipedia as wp

class Wiki:

    def __init__(self):
        pass

    def search_wikipedia(self,query_text: str) -> str:
        """
        This method return search result from inner wikipedia search bar
        :param query_text: <str> information for search
        :return: <str>search result
        """
        search_result: str = wp.search(query_text)
        return search_result

    def summary_wikipedia(self,query_text: str) -> str:
        """
        This method return summary about given text from Wikipedia
        :param query_text: <str> information for search
        :return: <str> summary of given text
        """
        summary_result: str = wp.summary(query_text)
        return summary_result

    def page_wikipedia(self,query_text: str) -> str:
        """
        This method return sumamry about given text from Wikipedia
        :param query_text: <str> information for search
        :return: <str> page of given text
        """
        page_result: str = wp.page(query_text)
        return str(page_result.title)

wiki_obj=Wiki()
for item in [wiki_obj.search_wikipedia("Atatürk"),wiki_obj.summary_wikipedia("Atatürk"),wiki_obj.page_wikipedia("Atatürk")]:
    print(item)
    print("----------------------------------------------------------------------------------------------------------------")