# how_to_use_template

|name|description|example|
|--|--|--|
|variable|將views傳送內顯示在模版指定的位置上|{{username}}|
|標籤|if 條件指令和for 迴圈指令|{%if found%}{%for item in items%}|
|單行註解|語法:{#註解文字#}|{#這是註解文字#}|
|文字|html 標籤或文字|`<title>`顯示的模板</`title>`|

## variable

變數可以是一般的變數，也可以使用字典變數或串列，分別以`{{變數}}`、`{{字典變數.鍵}}`、`{{串列.索引}}`語法來表示。

> [!CAUTION]
> template中使用的語法與python並不相同

|變數類型|template|python|說明|
|--|--|--|--|
|dict|{{dict.name}}|`dict[name]`|name是dict的key|
|method|{{obj1.show}}|obj1.show()|show()是obj1物件的方法|
|array|{{list1.0}}|`list1[0]`|list1是array。例如`list1=["a","b","c"]`|

## if syntax

- 單向判斷式
```html
{% if condition %}
    block
{% endif %}
```
- 雙向判斷式
```html
{% if condition %}
    block1
{% else %}
    block2
{% endif %}
```

- 多向判斷式
```html
{% if condition %}
    block1
{% elif %}
    block2
{% elif %}
    block3
{% else %}
    block4
{% endif %}
```

## for syntax

```html
{%% for 變數 in 串列 }
    block
```

- example

```python
list1=range(1,6)
```

```html
{% for i in list1 %}
    {{i}},
{% endfor %}
```