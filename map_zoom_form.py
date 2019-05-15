from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, SelectField, IntegerField, StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class MapForm(FlaskForm):
    """
    Form for users to add new energy bill
    """
    lat_min = FloatField('Latitude Start', validators=[DataRequired()], default=19.55)
    lat_max = FloatField('Latitude End', validators=[DataRequired()], default=20.55)
    lon_min = FloatField('Longitude Start', validators=[DataRequired()], default=49.55)
    lon_max = FloatField('Longitude End', validators=[DataRequired()], default=50.55)
    interpolation = SelectField('Interpolation', validators=[DataRequired()],
                                choices=[("1", "No interpolation"), ("2", "x2"), ("3", "x3"), ("5", "x5"), ("10", "x10"), ("25", "x25")], default=2)
    line_opacity = FloatField('Line opacity', validators=[DataRequired()], default=0)
    fill_opacity = FloatField('Fill opacity', validators=[DataRequired()], default=0.7)
    color = SelectField('Colors', choices=[(color, color) for color in [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']], default="Oranges")
    submit = SubmitField('Refresh')

    # TODO: validators