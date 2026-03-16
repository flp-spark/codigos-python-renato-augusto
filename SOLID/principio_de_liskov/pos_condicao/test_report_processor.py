from report_generator_interface import ReortGeneratorInterface


class TestReportProcessor:

    def process(self, report_generator: ReortGeneratorInterface):

        path = report_generator.generate()

        if not path:
            print('Arquivo não existe')

        # codigo para processar o arquivo de report