I've been dealing with some issues in our data pipeline the incoming data is all over the place. Wrote this function to process it, but I'm not sure if it's solid. The data could be lists of dicts, dicts with lists, nested keys, missing values, you name it. Need to make sure it doesn't break with unexpected inputs. Think you could come up with some unit tests for this? Not sure if I've thought of everything.

def process_data(data):
    result = []
    for item in data:
        try:
            value = item.get('value', 0.0)
            if isinstance(value, dict):
                nested_value = value.get('nested_value', 0.0)
                if isinstance(nested_value, list):
                    accum = 0.0
                    for v in nested_value:
                        accum += float(v)
                    result.append(accum)
                else:
                    result.append(float(nested_value))
            elif isinstance(value, list):
                for v in value:
                    result.append(float(v))
            else:
                result.append(float(value))
        except (ValueError, TypeError):
            continue
    total = sum(result)
    average = total / len(result) if result else 0.0
    return {'total': total, 'average': average, 'count': len(result)}