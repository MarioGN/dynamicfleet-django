from django.test import TestCase
from dynamicfleet.veiculos.forms import VehicleForm
from dynamicfleet.veiculos.models import Vehicle


class VehicleFormTest(TestCase):
    def test_form_has_fields(self):
        form = VehicleForm()
        expected = ['model', 'license_plate', 'year', 'state']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_model_is_required(self):
        form = self.make_validated_form(model=None)
        self.assertFormErrorCode(form, 'model', 'required')

    def test_license_is_required(self):
        form = self.make_validated_form(license_plate=None)
        self.assertFormErrorCode(form, 'license_plate', 'required')

    def test_year_is_required(self):
        form = self.make_validated_form(year=None)
        self.assertFormErrorCode(form, 'year', 'required')

    def test_state_is_required(self):
        form = self.make_validated_form(state=None)
        self.assertFormErrorCode(form, 'state', 'required')

    def test_license_is_unique(self):
        obj = Vehicle(
            model='Gol',
            license_plate='XYZ2284',
            year=2018,
        )
        obj.save()

        form = self.make_validated_form(license_plate='XYZ2284')
        self.assertFormErrorCode(form, 'license_plate', 'unique')

    def test_year_is_grater_than_1949(self):
        form = self.make_validated_form(year=1949)
        self.assertFormErrorCode(form, 'year', 'invalid value')

    def test_year_is_less_than_current_year(self):
        import datetime
        current_year = datetime.date.today().year + 1

        form = self.make_validated_form(year=current_year)
        self.assertFormErrorCode(form, 'year', 'invalid value')

    def test_error_message_invalid_year(self):
        form = self.make_validated_form(year=1949)
        self.assertFormErrorMessage(form, 'year', 'O ano de fabricação informado não é válido.')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(model='Gol', license_plate='XHJ9874', year=2020)
        data = dict(valid, **kwargs)
        form = VehicleForm(data)
        form.is_valid()

        return form

