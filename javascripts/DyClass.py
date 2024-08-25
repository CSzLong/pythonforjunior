class DynamicClassGenerator:
    def __init__(self, data: dict):
        # 确保字典只有一对键值对
        if len(data) != 1:
            raise ValueError("Dictionary must contain exactly one key-value pair.")

        # 获取字典的键和值
        self.class_name, attributes = next(iter(data.items()))

        # 确保值是一个字符串列表
        if not isinstance(attributes, list) or not all(isinstance(attr, str) for attr in attributes):
            raise ValueError("Value must be a list of strings.")

        # 动态创建类
        self.class_attributes = {attr: None for attr in attributes}
        self.class_attributes['to_dict'] = self.to_dict
        self.class_attributes['__repr__'] = self.__repr__

        # 动态添加 __init__ 方法
        def _init(self, *args, **kwargs):
            for attr in attributes:
                setattr(self, attr, kwargs.get(attr, None))

        self.class_attributes['__init__'] = _init
        self.new_class = type(self.class_name, (object,), self.class_attributes)

    def to_dict(self, instance, exclude=None):
        if exclude is None:
            exclude = []
        return {k: v for k, v in instance.__dict__.items() if k not in exclude}

    def __repr__(self, instance):
        class_name = instance.__class__.__name__
        attrs = ', '.join(f"{k}={v!r}" for k, v in instance.__dict__.items())
        return f"{class_name}({attrs})"

    def get_class(self):
        return self.new_class


# 示例使用
data = {
    "Person": ["name", "age", "gender"]
}
if __name__ == '__main__':

    # 创建类
    generator = DynamicClassGenerator(data)
    Person = generator.get_class()

    # 实例化对象并设置属性
    p = Person(name="张三", age=30, gender="男")

    # 打印属性
    print(p.name)  # 张三
    print(p.age)   # 30
    print(p.gender)  # 男

    # 打印字典表示
    print(p.to_dict(exclude=['age']))  # {'name': '张三', 'gender': '男'}

    # 打印对象表示
    print(p)  # Person(name='张三', age=30, gender='男')
