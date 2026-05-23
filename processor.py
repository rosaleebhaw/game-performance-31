import logging

class Processor:
    def __init__(self, data):
        self.data = data
        self.logger = logging.getLogger(__name__)

    def process_data(self):
        try:
            if not isinstance(self.data, list):
                raise ValueError("Data must be a list")

            processed = []
            for item in self.data:
                if not isinstance(item, int):
                    self.logger.warning(f"Skipping non-integer item: {item}")
                    continue
                if item < 0:
                    self.logger.warning(f"Negative value encountered: {item}")
                    continue
                processed.append(item ** 2)
            return processed

        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return []

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    p = Processor([1, 2, -3, 'four'])
    print(p.process_data())