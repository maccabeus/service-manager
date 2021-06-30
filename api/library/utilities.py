
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

    def is_slot_within_closing_hour(closing_hour, slot_end_time, multiplier=10000):
        """
        check if the ``slot_end_time`` is still within the ``closing_hour`` range

        if not, this work order must be schedule for the next day and we cannot alot time
        """
        if float(closing_hour) > 0:
            closing_hour_value= float(closing_hour) * multiplier
            # convers hour base. Since this is not . Note this is in hhmmss
        else:
            closing_hour_value= 0

        valid= (float(closing_hour_value) > float(slot_end_time))

        # print(closing_hour_value, "closing")
        # print(slot_end_time, "slot end")

        return valid
        # returns ``True`` if we still have time for schedule assignmen

