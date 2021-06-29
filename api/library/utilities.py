
class Utilities:
    """
    An APi wide messaging service for our applicaion
    """
    def response_formatter(error: bool= False, message: str=None, data=[]):
        """
        Create a message object for all our API response calls

        Args:
            error (bool, optional): [description]. Defaults to False.
            message ([str], optional): [description]. Defaults to None.
            data (list, optional): [description]. Defaults to [].

        Returns:
            [object]: dictionary object
        """                
        return ({'error': error, 'message': message, 'data': data})


    def validate_response(response_object,  message_found: str= "Record found",  message_not_found: str= "Record not found"):
        """
        Validate response returned ``response_object`` . We will either return data value of empty array
        rather than validating each returned data manually from each call, we will use this

        Args:
            respose_object (object): an iterable object
            message (str): The message to show when record not found
        """  

        if(len(response_object) <= 0):
            return ({'error': False, 'message':message_not_found, 'data':[]})
        """
        return an empty list for ``data``. This it to help while consuming the API
        """

        return ({'error': False, 'message':message_found, 'data':response_object.data})