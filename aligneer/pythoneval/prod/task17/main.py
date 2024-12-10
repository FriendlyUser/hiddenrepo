
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