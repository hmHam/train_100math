$(function () {
    var display_question = function (question) {
        $('input#answer').val('');
        $('#n_back_q').text(question);
    };
    var prepare_question = function (min, max) {
        return Math.floor(Math.random() * (max + 1 - min)) + min;
    }
    var check_answer = function (answer, input) {
        if (input === '') return false
        return +input === answer;
    };
    $('#start_nback').click(function () {
        // ゲームスタートしてボタンを削除
        var n = parseInt($('#n').data('n')) || 0;
        var i = 0;
        var interval = 2;
        var btn = $(this);
        btn.hide();
        var placeholder = btn.parent().find('span');
        placeholder.text('残り' + n + '問');
        // 問題を準備
        var questions = [];
        for (var j = 0; j < n; j++) {
            questions.push(prepare_question(1, 100));
        }
        var score = 0;
        var t = $('input#answer');
        t.focus();
        var id = setInterval(function () {
            display_question(questions[i]);
            setTimeout(function () {
                if (check_answer(questions[i], t.val())) {
                    score += 1;
                }
                i++;
                t.focus();
                placeholder.text('残り' + (n - i) + '問')
            })
            if (i == n) {
                console.log(score);
                placeholder.text('finish !');
                clearInterval(id);
            }
        }, interval * 1000);
    });
});