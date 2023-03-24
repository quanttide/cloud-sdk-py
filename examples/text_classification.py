"""
文本分类示例
"""

from cloud_sdk.baidubce import BaiduBceAPIClient


def classify_by_baidubce():
    client = BaiduBceAPIClient()
    result = client.topic("")
    print(result)


def main():
    classify_by_baidubce()


if __name__ == "__main__":
    main()
