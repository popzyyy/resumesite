import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import FileExtensionValidator
from django.forms import ModelForm, Textarea, TextInput, formset_factory, modelformset_factory, BaseModelFormSet, \
    NumberInput
from app.models import *
from django.db.models import Max


class GPAForm(forms.ModelForm):
    class Meta:
        model = GPA
        fields = ('class_name', 'class_grade', 'class_credits')


GPAFormSet = modelformset_factory(GPA, form=GPAForm, extra=4)


class InflationForm(forms.Form):
    today = datetime.date.today()
    year = today.year
    month = today.month

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    month_alt_choices = months[0: month - 2]

    end_month_choices = tuple([(month, month) for month in months])

    year_choice = [(i, i) for i in range(1913, year + 1)]
    start_month_choices = [
        ("January", "January"), ("February", "February"), ("March", "March"),
        ("April", "April"), ("May", "May"),
        ("June", "June"), ("July", "July"), ("August", "August"), ("September", "September"), ("October", "October"),
        ("November", "November"), ("December", "December")
    ]

    max_year = Inflation.objects.aggregate(Max('year'))['year__max']

    start_money = forms.DecimalField(initial=1, label='$', min_value=.01, decimal_places=2, max_digits=18)
    month_start = forms.ChoiceField(choices=end_month_choices, initial="January", label='')
    year_start = forms.TypedChoiceField(choices=year_choice, coerce=int, initial="2000", label='')
    month_end = forms.ChoiceField(choices=start_month_choices, initial="January", label='')
    year_end = forms.TypedChoiceField(choices=year_choice, coerce=int, initial=max_year, label='')


class LineForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 8, 'cols': 40, 'margin': '0px', 'padding': '0px', 'border': '0px'}
                              ))


class DateForm(forms.Form):
    date1 = forms.DateField(widget=forms.SelectDateWidget(years=range(1, 2250), attrs={'style': 'width: 10em;'}))
    date2 = forms.DateField(widget=forms.SelectDateWidget(years=range(1, 2250), attrs={'style': 'width: 10em;'}))


class DateForm2(forms.Form):
    math_choices = [('Subtract', 'Subtract'), ('Add', 'Add')]

    math_type = forms.ChoiceField(choices=math_choices)
    date_between = forms.DateField(label='Start Date', initial=datetime.datetime.now(),
                                   widget=forms.SelectDateWidget(years=range(600, 2250),
                                                                 attrs={'style': 'width: 10em;'}))

    day = forms.IntegerField(label='Days', min_value=0, max_value=2500,
                             widget=forms.TextInput(attrs={'style': 'width: 10em;'}))
    month = forms.IntegerField(label='Months', min_value=0, max_value=2500,
                               widget=forms.TextInput(attrs={'style': 'width: 10em;'}))
    year = forms.IntegerField(label='Years', min_value=0, max_value=500,
                              widget=forms.TextInput(attrs={'style': 'width: 10em;'}))


class TimeForm(forms.Form):
    timefield1 = forms.DateTimeField(widget=forms.SplitDateTimeWidget(attrs={'style': 'width: 10em;'}))
    timefield2 = forms.DateTimeField(widget=forms.SplitDateTimeWidget(attrs={'style': 'width: 10em;'}))


class DeathForm(forms.Form):
    death_time = forms.DateTimeField(widget=forms.SplitDateTimeWidget(attrs={'style': 'width: 10em;'}))


class DistanceForm(forms.Form):
    ###### MEASUREMENTS
    distance_to = forms.DecimalField(
        min_value=-99999,
        max_value=99999,
        max_digits=100000,
        decimal_places=9,
        initial="",
        disabled=True,
        required=False,
        widget=(
            forms.HiddenInput()
        ))

    distance_from = forms.DecimalField(
        min_value=-99999,
        max_value=99999,
        max_digits=100000,
        decimal_places=9,
        widget=forms.TextInput(attrs={'style': 'width: 8em;'})
    )

    # imperial
    DISTANCE_CHOICES = (
        ("feet", "Feet"),
        ("inch", "Inch"),
        ("yard", "Yard"),
        ("mile", "Mile"),

        # metric
        ("terameter", "Terameter"),
        ("gigameter", "Gigameter"),
        ("megameter", "Megameter"),
        ("kilometer", "Kilometer"),
        ("hectometer", "Hectometer"),
        ("decameter", "Decameter"),
        ("meter", "Meter"),
        ("decimeter", "Decimeter"),
        ("centimeter", "Centimeter"),
        ("millimeter", "Millimeter"),
        ("micrometer", "Micrometer"),
        ("nanometer", "Nanometer"),
        ("picometer", "Picometer"),
        ("femtometer", "Femtometer"),
        ("attometer", "Attometer"),
        ("lightyear", "Lightyear"),
        ("freedom_unit", "Freedom_Unit"),
    )

    unit_from = forms.ChoiceField(
        choices=DISTANCE_CHOICES,
        widget=forms.Select(attrs={'style': 'width: 14em;'})
    )
    unit_to = forms.ChoiceField(
        choices=DISTANCE_CHOICES,
        widget=forms.Select(attrs={'style': 'width: 14em;'})
    )


class TemperatureForm(forms.Form):
    ##### TEMPERATURE
    temperature_to = forms.DecimalField(
        min_value=-99999,
        max_value=99999,
        max_digits=20,
        decimal_places=12,
        initial=None,
        required=False,
        disabled=True,
        widget=forms.TextInput(attrs={'style': 'width: 8em;', 'readonly': 'readonly'})
    )

    temperature_from = forms.DecimalField(
        min_value=-99999,
        max_value=99999,
        max_digits=20,
        decimal_places=12,
        widget=forms.TextInput(attrs={'style': 'width: 8em;'})
    )

    TEMP_CHOICES = (
        ("fahrenheit", "Fahrenheit"),
        ("celsius", "Celsius"),
        ("kelvin", "Kelvin"),
        ("rankine", "Rankine"),

    )

    unit_from = forms.ChoiceField(
        choices=TEMP_CHOICES,
        widget=forms.Select(attrs={'style': 'width: 14em;'})
    )
    unit_to = forms.ChoiceField(
        choices=TEMP_CHOICES,
        widget=forms.Select(attrs={'style': 'width: 14em;'})
    )


class VolumeForm(forms.Form):
    #### Volume
    ##### TEMPERATURE
    volume_to = forms.DecimalField(
        min_value=-99999,
        max_value=99999,
        max_digits=20,
        decimal_places=12,
        initial=None,
        required=False,
        disabled=True,
        widget=forms.TextInput(attrs={'style': 'width: 8em;', 'readonly': 'readonly'})
    )

    volume_from = forms.DecimalField(
        min_value=-99999,
        max_value=99999,
        max_digits=20,
        decimal_places=12,
        widget=forms.TextInput(attrs={'style': 'width: 8em;'})
    )

    VOLUME_CHOICES = (
        # Imperial
        ("teaspoon", "Teaspoon"),
        ("tablespoon", "Tablespoon"),
        ("fluid_ounce", "Fluid Ounce"),
        ("cup", "Cup"),
        ("pint", "Pint"),
        ("quart", "Quart"),
        ("gallon", "Gallon"),
        ("barrel", "Barrel"),

        # Metric (CRINGE)
        ("milliliter", "Milliliter"),
        ("centiliter", "Centiliter"),
        ("deciliter", "Deciliter"),
        ("liter", "Liter"),
        ("decaliter", "Decaliter"),
        ("hectoliter", "Hectoliter"),
        ("kiloliter", "Kiloliter"),
    )

    unit_from = forms.ChoiceField(
        choices=VOLUME_CHOICES,
        widget=forms.Select(attrs={'style': 'width: 14em;'})
    )
    unit_to = forms.ChoiceField(
        choices=VOLUME_CHOICES,
        widget=forms.Select(attrs={'style': 'width: 14em;'})
    )


class ETLForm(forms.Form):
    file_uploads = forms.FileField(
        required=True,
        help_text=".csv files only! 2MB file size max!",
        validators=[FileExtensionValidator(allowed_extensions=["csv"])],
        error_messages={
            "required": "Please select a file to upload.",
            "invalid": "This is not a valid file.",
        },
    )
