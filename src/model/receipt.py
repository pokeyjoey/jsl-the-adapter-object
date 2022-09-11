class Receipt:
    mapping = {'location_name': 'restaurant_name', 
               'location_address': 'address',
               'obligation_end_date_yyyymmdd': 'end_date',
               'total_receipts': 'total'}
    api_field_names = mapping.keys()
    columns = ['total', 'address', 'end_date', 'restaurant_name']


    def __init__(self, **kwargs):
        # set class attributes from the keyword arguments
        for k, v in kwargs.items():
            if k in self.api_field_names:
                setattr(self, self.mapping.get(k), v)

