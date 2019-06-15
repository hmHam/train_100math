import random
from django import forms, views
from train_100math.app.forms import Train100MathForm
from django.shortcuts import render


Q_COUNT = 50


def hello_template(request):
    return render(request, 'index.html')


# Create your views here.
class Train100MathView(views.View):
    ops = ['*', '+', '-', '/%']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request):
        form_item = {}
        for i in range(Q_COUNT):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            op = self.ops[random.randint(0, 100) % 4]
            expr = '%d %s %d = ' % (x, op, y)
            form_item.update({
                expr: forms.CharField(
                    label=expr,
                    required=True,
                    initial=0
                )
            })
        d = type('DynamicForm', (Train100MathForm,), form_item)({})

        context = {}
        context['form'] = []
        keys = sorted(d.fields, key=lambda v: v[0])
        base = 5
        for i in range(int(Q_COUNT / base)):
            f = []
            ks = keys[base * i:base * (i + 1)]
            for k in ks:
                f.append(d[k])
            context['form'].append(f)
        context['b'] = base
        return render(request, 'train.html', context)

    def post(self, request):
        form = {}
        for key in request.POST.keys():
            if key != 'csrfmiddlewaretoken':
                form[key] = request.POST[key]
        # 採点
        success_count = 0
        print(form)
        for fk, fv in form.items():
            print(fk, fv)
            x, op, y = fk.split()[:-1]
            expr = '%d %s %d' % (int(x), '%s', int(y))
            # 割り算
            if op == '/%':
                result = []
                # 割り算の時は、商 あまり
                ans = fv.split()
                for a, o in zip(ans, list(op)):
                    result.append(int(a) == eval(expr % o))
                if all(result):
                    success_count += 1
            else:
                result = eval(expr % op)
                if result == int(fv):
                    success_count += 1
        context = {}
        context['success'] = success_count
        context['total'] = Q_COUNT
        context['rate'] = '%.2f' % (success_count * 100 / Q_COUNT,)
        return render(request, 'answered.html', context)


class NBackView(views.View):

    def get(self, request):
        context = {}
        context['n'] = 5
        return render(request, 'n_back.html', context)