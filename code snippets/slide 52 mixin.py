class ColorMixin:
    is_colored = True
    
    def __init__(self, *args, **kwargs):
        color = kwargs.get('color', None)
        if color is None:
            color = random.choice(COLORS)
            kwargs['color'] = color
        self.color = color
        super().__init__(*args, **kwargs)

