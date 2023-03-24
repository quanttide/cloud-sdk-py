"""
文本分类示例
"""

from cloud_sdk.baidubce import BaiduBceClient


def classify_by_baidubce():
    client = BaiduBceClient()
    result = client.topic("")
    print(result)


def main():
    classify_by_baidubce()


if __name__ == "__main__":
    main()
