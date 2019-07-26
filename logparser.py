#!/usr/bin/env  python3



import re
pattern = '(?P<host>.+?)\s(?P<identity>.+?)\s(?P<user>.+?)\s\[(?P<timestamp>.+?)\]\s\"(?P<request>.+?)\"\s(?P<status>\d{1,})\s(?P<size>\d{1,})'

def parser(s):
        """
        return type : dict()
        return format: {
                       host:str , identity:str , user:str ,
                                           time:str ,request:str , status:str ,
                                           size:str , referer:str, agent:str
                                        }
        returns None if failed.
        """

        try:
                parts = re.match(pattern,s)
                return parts.groupdict()
        except Exception as err:
                print(err)