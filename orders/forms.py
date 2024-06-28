class OrdersForm(forms.ModelForm):
    states=[
        ('AP','Andra Pradesh'),('AR','Arunchal Pradesh'),('AS','Assam'),
        ('BR','Bihar'),('CG','Chhattisgarh'),('GJ','Gujrat'),('HR','Haryana'),
        ('HP','Himachal Pradesh'),('MP','Madya Pradesh'),('MH','Maharashtra'),
        ('MZ','Mizoram'),('NL','Nagaland'),('OD','Odisa'),('PB','Punjab',)
        ]

        first_name=forms.CharField(max_length=50,widget=form.TextInput(attrs={'class':'form-control'}))
        last_name=forms.CharField(max_length=50,widget=form.TextInput(attrs={'class':'form-control'}))
        phone=forms.CharField(max_length=10,widget=form.TextInput(attrs={'class':'form-control'}))
        email=forms.CharField(max_length=100,widget=form.TextInput(attrs={'class':'form-control'}))
        address=forms.CharField(max_length=100,widget=form.TextInput(attrs={'class':'form-control'}))
        country=forms.CharField(max_length=100,widget=form.TextInput(attrs={'class':'form-control'}))
        state=forms.CharField(choices=states,widget=form.TextInput(attrs={'class':'form-control'}))
        city=forms.CharField(max_length=100,widget=form.TextInput(attrs={'class':'form-control'}))

        class Meta:
            model=Orders
            fields=['first_name','last_name','phone','email','address','country','state']
