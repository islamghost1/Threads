import conf
import requests
import json


def _POST_(route, dict):
    """POST is used to send data to a server to create/update a resource

    Args:
        path (str): route to API
        dict (dict): body dictionnary 
    """
    try:

        if route:   # check if apth  is not empty
            url = "{}{}".format(conf.PATH, route)

            bodyDict = {

                "username": conf.USERNAME,
                "password": conf.PASSWORD,
                "environment": conf.ENVIRONMENT,
                "role": "*ALL"

            }

            # append dict param to the deafault dict usin update method
            bodyDict.update(dict)

            payload = json.dumps(bodyDict)

            headers = {

                'Content-Type': 'application/json',
                'Cookie': 'JSESSIONID=K3o-MTiomh7KS_1BJltTxABPO5dJ4VCKam0PyRwxfZ0ndFhX08VO!-1108609794'

            }
            # POST request
            response = requests.request(
                "POST", url, headers=headers, data=payload)

            print(response.status_code)
            # returning response text and response code
            return [response.text, response.status_code]
        else : 
            return "Route is empty "
    except Exception as e:
        # return exception
        print(str(e))
        return str(e)
_POST_("","")        
