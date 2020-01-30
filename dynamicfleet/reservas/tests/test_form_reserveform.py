from datetime import datetime, timedelta
from django.test import TestCase
from dynamicfleet.reservas.forms import ReserveForm


class ReserveFormTest(TestCase):
    def test_form_has_fields(self):
        form = ReserveForm()
        expected = ['start', 'end', 'state']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_start_is_required(self):
        form = self.make_validated_form(start=None)
        self.assertFormErrorCode(form, 'start', 'required')

    def test_end_is_required(self):
        form = self.make_validated_form(end=None)
        self.assertFormErrorCode(form, 'end', 'required')

    def test_state_is_required(self):
        form = self.make_validated_form(state=None)
        self.assertFormErrorCode(form, 'state', 'required')

    def test_start_date_cannot_be_less_than_today(self):
        start = datetime.today() - timedelta(days=1)
        form = self.make_validated_form(start=start)
        self.assertFormErrorCode(form, 'start', 'invalid value')

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
        valid = dict(start=datetime.today(), end=datetime.today() + timedelta(days=2))
        data = dict(valid, **kwargs)
        form = ReserveForm(data)
        form.is_valid()

        return form