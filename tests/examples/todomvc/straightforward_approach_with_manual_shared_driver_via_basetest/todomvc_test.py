# MIT License
#
# Copyright (c) 2015-2019 Iakiv Kramarenko
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from selene.support.past import browser
from selene.support.conditions import be
from selene.support.conditions import have
from tests.base_test import *

from selene.support.past.bys import by_link_text
from selene.support.past.conditions import exact_text
from selene.support.past.support.jquery_style_selectors import s, ss

APP_URL = 'https://todomvc4tasj.herokuapp.com/'


class TestTodoMVC(BaseTest):

    def test_filter_tasks(self):
        browser.open_url(APP_URL)
        clear_completed_js_loaded = "return $._data($('#clear-completed').get(0), 'events').hasOwnProperty('click')"
        browser.wait_to(have.js_returned_true(clear_completed_js_loaded))

        s('#new-todo').should(be.enabled).set_value('a').press_enter()
        s('#new-todo').should(be.enabled).set_value('b').press_enter()
        s('#new-todo').should(be.enabled).set_value('c').press_enter()

        ss("#todo-list>li").should(have.texts('a', 'b', 'c'))

        ss("#todo-list>li").element_by(exact_text('b')).find(".toggle").click()

        s(by_link_text("Active")).click()
        ss("#todo-list>li").filtered_by(be.visible).should(have.texts('a', 'c'))

        s(by_link_text("Completed")).click()
        ss("#todo-list>li").filtered_by(be.visible).should(have.texts('b'))


