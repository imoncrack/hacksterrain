def get_data_from_dynamodb():
    try:
            import boto3
            from boto3.dynamodb.conditions import Key, Attr

            dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='ASIAWF6XSDNSNOPLHF5P', aws_secret_access_key='83mhTaO4q1HmE4U4P31/ieRKkfUXYVtaAn6W8Skk', aws_session_token='FwoGZXIvYXdzENj//////////wEaDFty6zj/NLuhO1k4mSLJAbUK/npjrakhQ52+XzST10WX+VqtuxLjRCOtmCHGMa/7z6SUhlVsOF3dTy40atCnu9SILW98WaIUORClmuMoTcNOCfEMH+kkqhy0gkb1YPvF/PzJMsauzysl48ifmlfZjJs/jzuh8Xj5Apz4FWeI9CB2tRhJK50RwUUHEiuRNTvX7KiJesfysD7kOz24jTFwyel+RjKdcwZG3e5+ViOPbq1ro8lCmRKTTyU990wiOQ7uFnc+pe6pPqAEupUo1JGF0EAK5BSpmrVcgiiM1dTyBTItfXy8x21xaMwL+YULiSftatrolirSbr8kSNdm2+0jGjrOMv2yuAFuZVCPQO57')


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
