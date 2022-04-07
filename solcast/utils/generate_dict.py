from isodate import parse_datetime, parse_duration


def generate_dict(items: list[dict]) -> list[dict]:
    result = []

    for item in items:
        # Convert period_end and period. All other fields should already be
        # the correct type
        item['period_end'] = parse_datetime(item['period_end'])
        item['period'] = parse_duration(item['period'])

        result.append(item)

    return result
