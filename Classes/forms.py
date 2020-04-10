from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from Settings import Config

class FormPlayerWorldranking(FlaskForm):
    org = SelectField('Ranking Organisation', choices=[('atp', 'ATP'), ('wta', 'WTA')])
    type = SelectField('Match Type', choices=[('singles', 'singles'), ('doubles', 'doubles')])
    language = SelectField('Wikipedia Language', choices=[('en', 'en'), ('de', 'de'), ('cs', 'cs'), ('es', 'es'),
                                                          ('fr', 'fr'), ('it', 'it'), ('ja', 'ja'), ('pl', 'pl'),
                                                          ('pt', 'pt'), ('ro', 'ro'), ('ru', 'ru'), ('sv', 'sv'),
                                                          ('zh', 'zh')])
    cut = IntegerField('Ranking Cut', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Request')

class FormPlayerTournamentwins(FlaskForm):
    org = SelectField('Ranking Organisation', choices=[('atp', 'ATP')])
    type = SelectField('Match Type', choices=[('singles', 'singles'), ('doubles', 'doubles')])
    player = StringField('Player-ID', validators=[DataRequired()])
    language = SelectField('Wikipedia Language', choices=[('de', 'de')])
    submit = SubmitField('Request')