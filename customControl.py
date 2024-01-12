def smartInput(msg:str="",datatype=str,bounds=None,validinput=None,case:str="lower"):
    while True:
        try:
            user = datatype(input(msg))
            if type(user) == str:
                if case == "upper":
                    user = user.upper()
                elif case == "lower":
                    user = user.lower()
                
            if bounds != None:
                if not bounds[0] <= user <= bounds[1]:
                    raise ValueError
            if validinput != None:
                if user not in validinput:
                    raise ValueError
            break
        except ValueError:
            continue
    return user

# Custom Vector2 Implementation
class Vector2:
    # Initilize class with a x and y value
    def __init__(self,x:int|float,y:int|float) -> None:
        self._x = x
        self._y = y

    # Define properties for x and y
    @property
    def x(self) -> int|float:
        return self._x
    
    @x.setter
    def x(self, value:int|float):
        self._x = value

    @property
    def y(self) -> int|float:
        return self._y
    
    @y.setter
    def y(self, value:int|float):
        self._y = value

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"
        
    # Vector Math Functions
    def __add__(self, other: 'Vector2 | int | float') -> 'Vector2':
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x + other, self.y + other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __sub__(self, other: 'Vector2 | int | float') -> 'Vector2':
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x - other, self.y - other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __mul__(self, other: 'Vector2 | int | float') -> 'Vector2':
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __truediv__(self, other: 'Vector2 | int | float') -> 'Vector2':
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            if other != 0:
                return Vector2(self.x / other, self.y / other)
            else:
                raise ValueError("Division by zero.")
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")
    
    def __iter__(self):
        yield self.x
        yield self.y

# Custom Vector3 Implementation  
class Vector3:
    # Initilize class with a x and y value
    def __init__(self,x:int|float,y:int|float,z:int|float) -> None:
        self._x = x
        self._y = y
        self._z = z

    # Define properties for x and y
    @property
    def x(self) -> int|float:
        return self._x

    @property
    def y(self) -> int|float:
        return self._y
    
    @property
    def z(self) -> int|float:
        return self._z

    def __str__(self):
        return f"Vector2({self.x}, {self.y}, {self.z})"
    
    # Math Functions
    def __add__(self,other:'Vector3 | int | float') -> 'Vector3':
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __sub__(self,other:'Vector3') -> 'Vector3':
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (int,float)):
            return Vector3(self.x - other, self.y - other, self.z - other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")
    
    def __mul__(self,scalar:'Vector3') -> 'Vector3':
        if isinstance(scalar, Vector3):
            return Vector3(self.x * scalar.x, self.y * scalar.y, self.z * scalar.z)
        elif isinstance(scalar, (int, float)):
            return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
        else:
            raise TypeError(f"Unsupported operand type: {type(scalar)}")

    def __truediv__(self, scalar: 'Vector3 | int | float') -> 'Vector3':
        if isinstance(scalar, Vector3):
            return Vector3(self.x / scalar.x, self.y / scalar.y, self.z / scalar.z)
        elif isinstance(scalar, (int, float)):
            if scalar != 0:
                return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)
            else:
                raise ValueError("Division by zero.")
        else:
            raise TypeError(f"Unsupported operand type: {type(scalar)}")
    
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z