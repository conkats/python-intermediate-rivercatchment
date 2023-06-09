#!/usr/bin/env python3
"""Software for managing and tracking environmental data from our field project."""

import argparse

from catchment import models, views


def main(args):
    """The MVC Controller of the environmental data system.
    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    infiles = args.infiles
    if not isinstance(infiles, list):
        infiles = [args.infiles]

    for filename in infiles:
        measurement_data = models.read_variable_from_csv(filename, args.measurements)


        if args.view == 'visualize':
            view_data = {'daily sum': models.daily_total(measurement_data),
                         'daily average': models.daily_mean(measurement_data),
                         'daily max': models.daily_max(measurement_data),
                         'daily min': models.daily_min(measurement_data)}
        
            views.visualize(view_data)

        elif args.view == 'record':
            measurement_data = measurement_data[args.site]
            site = models.Site(args.site)
            site.add_measurement(args.measurements, measurement_data)

            views.display_measurement_record(site)


def parse_cli_arguments():
    """Definitions and logic tests for the CLI argument parser"""
    
    parser = argparse.ArgumentParser(
        description='A basic environmental data management system')
    
    req_group = parser.add_argument_group('required arguments')

    parser.add_argument(
        'infiles',
        nargs = '+',
        help = 'Input CSV(s) containing measurement data')

    req_group.add_argument(
        '-m', '--measurements',
        help = 'Name of measurement data series to load',
        required = True)

    parser.add_argument(
        '--view',
        default = 'visualize',
        choices = ['visualize', 'record'],
        help = 'Which view should be used?')

    parser.add_argument(
        '--site',
        type = str,
        default = None,
        help = 'Which site should be displayed?')
    
    args = parser.parse_args()
    
    if args.view == 'record' and args.site is None:
        parser.error("'record' --view requires that --site is set")

    return args


if __name__ == "__main__":

    args = parse_cli_arguments()

    main(args)