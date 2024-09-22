#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from app import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    type = db.Column(db.String(50))

    def __repr__(self):
        return f'<Pet {self.name}>'