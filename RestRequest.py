import conf
import requests
import json
#import requests.exceptions


def _POST_(route, dic):
    """POST is used to send data to a server to create/update a resource

    Args:
        path (str): route to API
        dict (dict): body dictionnary 

    Returns:
        _type_: status code , response text 
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

            # check if dic is a dictionary
            if isinstance(dic, dict):
                # if token key is in dictionnary we delete pw and username from bodyDict
                token = "token"
                if token in dic:
                    del bodyDict["username"]
                    del bodyDict["password"]
                    # append dic param to the deafault bodyDict using update method
                    bodyDict.update(dic)

            payload = json.dumps(bodyDict)

            headers = {

                'Content-Type': 'application/json',
                # 'Cookie': 'JSESSIONID=K3o-MTiomh7KS_1BJltTxABPO5dJ4VCKam0PyRwxfZ0ndFhX08VO!-1108609794'

            }
            # POST request
            response = requests.request(
                "POST", url, headers=headers, data=payload)
            # raise exception code in case of error
            response.raise_for_status()

            # returning response text and response code
            #print(response.text, response.status_code)
            return [response.text, response.status_code]
        else:
            #print("Route is empty ")
            return 404
    except requests.exceptions.HTTPError as e:
        # Maybe set up for a retry, or continue in a retry loop
        #print(f"error : {e.response.status_code}")
        #print(f"error : {e.response.text}")

        return e.response.status_code, e.response.text
    except Exception as e:
        #print(e)
        return 500




