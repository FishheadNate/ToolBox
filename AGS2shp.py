#!/usr/bin/env python3

import argparse
import logging
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def write_service_file(REST_API, dst_src):
    logging.info(' Cleaning services.txt')
    service_file = open('services.txt', 'w')
    service_file.close()
    service_file = open('services.txt', 'a')
    logging.info(' Writing details to services.txt')
    service_file.write(REST_API + '|' + dst_src + '|1000')
    service_file.close()


def call_AGStoShapefile():
    logging.info(' Running AGStoShapefile')
    subprocess.run('mkdir AGStoShapefile_Output', shell=True)
    subprocess.run('agsout -s services.txt -o AGStoShapefile_Output -S', shell=True)


def run(args):
    REST_API = args.REST_API
    dst_src = args.dst_src
    write_service_file(REST_API, dst_src)
    call_AGStoShapefile()
    logging.info(' Done\n')


def main():
    parser = argparse.ArgumentParser(description='Script to run AGStoShapefile by TannerGeo and return the GeoJSON & shapefile to your current directory. https://github.com/tannerjt/AGStoShapefile/blob/master/LICENSE.txt')
    parser.add_argument('-src', help='ESRI REST API for target map service layer', dest='REST_API', required=True)
    parser.add_argument('-dst', help='GeoJSON and shapefile output name', dest='dst_src', required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
