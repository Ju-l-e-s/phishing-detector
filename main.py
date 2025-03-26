from logger_config import setup_logger
from url_checks import URLAnalyzer


def main():
    """
    Main function to set up logging, instantiate the URLAnalyzer, and analyze test URLs.

    :param: None
    :return: None
    :rtype: None
    """
    setup_logger()
    analyzer = URLAnalyzer()

    test_urls = [
        "http://tamanna800.github.io/amazon", # bad url, don't click on it
        "https://drive.google.com/uc?export=download&id=1UnU9ydYXvBsgDAS_xzEWlzcaiV6O_QdT" # bad url, don't click on it
        # "https://secure-paypal.com/verify-account?user=martin&password=password",
        # "https://secure-paypa1.com/",
        # "https://bit.ly/3abcxyz",
        # "https://google.com"
    ]

    for url in test_urls:
        analyzer.analyze_url(url)


if __name__ == "__main__":
    main()
