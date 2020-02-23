def get_data_from_dynamodb():
    try:
            import boto3
            from boto3.dynamodb.conditions import Key, Attr

            dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='ASIAWF6XSDNSKHZ2QS6L', aws_secret_access_key='Ko0uxT833U2pzl5rvI6CYfLl90EMRDaIRid1tWbk', aws_session_token='FwoGZXIvYXdzEKX//////////wEaDPv9yUemXsHjZTaidyLJAU5V6GvqrDllQdCnxS33h0KqYeVa9dVGkPS5/ieP0Eeyf5ZT+OXIazrf8ecl/vKC8bGzlqh2rP9BET23fDvkt8CxGyz61h8HJ2XJziNaPJV5qGxrNwtIzL21HDe2NyszEkSqT6zrB0SVEclsn3oNCDWs9QuWwQ+xLNbhstsozEyTv7kdBQvW4JdVuvGsuR9MowOmm1CyaGmxJFSyaxvroNSMhE7kgS1bxx03cCbPdS51d8XaWLk6vVVgiaUSfkrZZ0hlcA3R3Er7nCj/xMnyBTItITEFFn/nWdp4DjRWS1M8C6wXlbj8hnGrapCeMb9VuQrNd64BPUwou1heoyak')


            startdate = '2020-02'
	    table = dynamodb.Table('iotdata')

            response = table.query(
                KeyConditionExpression=Key('deviceid').eq('deviceid_ZhiQuan') 
                                      & Key('datetimeid').begins_with(startdate),
                ScanIndexForward=False
            )

            items = response['Items']

            n=10 # limit to last 10 items
            data = items[:n]
            data_reversed = data[::-1]

            return data_reversed

    except:
        import sys
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])


if __name__ == "__main__":
    get_data_from_dynamodb()
