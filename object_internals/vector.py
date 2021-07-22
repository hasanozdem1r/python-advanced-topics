class Vector:

    def __init__(self,**coords):
        private_coords={'_'+k:v for k,v in coords.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name):
        private_name="_"+name
        return getattr(self,private_name)

    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute {!r}".format(name))

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                k=k[1:],
                v=self.__dict__[k])
                for k in sorted(self.__dict__.keys())))

v=Vector(p=3,q=8)
print(v.__dict__)
print(v.p,v.q)
print(dir(v))
