# Farmsubsidy.org

This code runs farmsubsidy.org.  Please read INSTALL if you are interested in setting it up yourself, and contact symroe (sym@ the projects domain name or @symroe on twitter) for help and information.

If you are interested in the project in general, please contact team@the project domain name.


These management commands may be of interest:

    python manage.py populate -c DE
    python manage.py payment_totals
    python manage.py transparency_index


For Deployment:
python manage.py collectstatic

SQL to make totals default to 0.0. Execute manually (not done by migrations):

ALTER TABLE data_recipient ALTER COLUMN total SET DEFAULT 0.0;
ALTER TABLE data_countryyear ALTER COLUMN total SET DEFAULT 0.0;
ALTER TABLE data_recipientyear ALTER COLUMN total SET DEFAULT 0.0;
ALTER TABLE data_scheme ALTER COLUMN total SET DEFAULT 0.0;
ALTER TABLE data_schemeyear ALTER COLUMN total SET DEFAULT 0.0;
ALTER TABLE data_recipientschemeyear ALTER COLUMN total SET DEFAULT 0.0;
ALTER TABLE data_totalyear ALTER COLUMN total SET DEFAULT 0.0;
