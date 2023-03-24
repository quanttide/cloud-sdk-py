"""
百度智能云
"""

import requests

from cloud_sdk.config import settings


class BaiduBceClient:
    def __init__(self):
        self.access_token = self.get_access_token()

    def get_access_token(self) -> str:
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": settings.API_KEY, "client_secret": settings.SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))

    def topic(self, payload):
        """

        https://ai.baidu.com/ai-doc/NLP/wk6z52gxe

        :param payload:
        :return:
        ```json
        {
            "log_id": 3591049593939822907,
            "item": {
                "lv2_tag_list": [
                    {
                        "score": 0.877436,
                        "tag": "足球"
                    },
                    {
                        "score": 0.793682,
                        "tag": "国际足球"
                    },
                    {
                        "score": 0.775911,
                        "tag": "英超"
                    }
                ],
                "lv1_tag_list": [
                    {
                        "score": 0.824329,
                        "tag": "体育"
                    }
                ]
            }
        }
        ```
        """
        url = f"https://aip.baidubce.com/rpc/2.0/nlp/v1/topic?charset=utf-8&access_token={self.access_token}"
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
