def parse_json(py_dict: dict):

    keys = ['title', 'x.axis.label', 'x.axis.unit', 'y.axis.label', 'y.axis.unit', 'data']
    for key in keys:
        if not key in py_dict:
            raise KeyError('invalid json format')
    
    if len(py_dict) != len(keys):
        raise KeyError('invalid json format')
    
    data_keys = ['legend', 'x', 'y']
    for line in py_dict['data']:
        for key in data_keys:
            if not key in line:
                raise KeyError('invalid json format')
        if len(line) != len(data_keys):
            raise KeyError('invalid json format')
        if len(line['x']) != len(line['y']):
            raise ValueError('inconsistent data size')
        
        x_values = []
        y_values = []
        for x_value in line['x']:
            x_values.append(float(x_value))
        for y_value in line['y']:
            y_values.append(float(y_value))

        line['x'] = x_values
        line['y'] = y_values
    
    return py_dict