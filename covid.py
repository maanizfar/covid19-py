#!/usr/bin/env python3
import api
import argparse
from prettytable import PrettyTable


common_fields = ["Today's Cases", "Total Cases",
                 "Today's Death", "Total Death", "Today's Recovered", "Total Recovered"]


def create_row(data, is_world=False):

    if is_world:
        first_column = 'World'
    else:
        first_column = data['Country']

    return[first_column, data["NewConfirmed"], data["TotalConfirmed"],
           data["NewDeaths"], data["TotalDeaths"], data["NewRecovered"], data["TotalRecovered"]]


def show_world_data(data):
    worlds_data = data['Global']

    x = PrettyTable()
    x.field_names = ["", ] + common_fields
    x.add_row(create_row(worlds_data, True))
    print(x)


def show_country_data(data, countrySlug):
    countries_data = data['Countries']

    x = PrettyTable()
    x.field_names = ["Country", ] + common_fields

    country = {}

    for c in countries_data:
        if c['Slug'] == countrySlug:
            country = c
            break

    if not country:
        print(f"Country {countrySlug} not found")
        return

    x.add_row(create_row(countries_data))

    print(x)


def show_all_data(data):
    worlds_data = data['Global']

    x = PrettyTable()
    x.field_names = ["Country", ] + common_fields

    x.add_row(create_row(worlds_data))

    d = data['Countries']
    for country in d:
        x.add_row([country["Country"], country["NewConfirmed"], country["TotalConfirmed"],
                   country["NewDeaths"], country["TotalDeaths"], country["NewRecovered"], country["TotalRecovered"]])

    print(x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-w', '--world', help="Show world's data", action='store_true')
    parser.add_argument(
        '-c', '--country', help="Show a country's data")
    args = parser.parse_args()

    data = api.get_summary()
    if data:
        if args.world:
            show_world_data(data)
        elif args.country:
            countrySlug = args.country.lower().replace(' ', '-')
            show_country_data(data, countrySlug)
        else:
            show_all_data(data)
