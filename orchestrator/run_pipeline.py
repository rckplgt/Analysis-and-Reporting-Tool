import yaml
from dbconnection.excel_connection import load_excel
from data_management.data_loader import clean_data
from analytics.analytics import generate_summary
from analytics.analytics import get_user_summary
from reporting.report_writer import generate_report

def run():
    config = yaml.safe_load(open("config/settings.yaml"))

    df = load_excel(config["input_file"])
    df = clean_data(df)
    summary = generate_summary(df)
    user_summary = get_user_summary(df)
    generate_report(user_summary, config["output_report"])

    print(f"Report generated: {config['output_report']}")
