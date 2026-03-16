from report_generator_interface import ReortGeneratorInterface


class S3ReportGenerator(ReortGeneratorInterface):

    def generate(self) -> str:

        # codigo para criar o report e salvar na s3

        report_name = f'{'Nome do arquivo'}.txt'

        return f'https://s3.amazon.com/mybucket/{report_name}'