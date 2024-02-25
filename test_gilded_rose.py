# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        expect_return = [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]
        for actual, expect in zip(gr.get_items_by_name(vest), expect_return):
            assert self.compare(actual, expect)

    def test_vest_item_quality_not_zero(self):
        vest = "test2"
        items = [Item(vest, 1, 2), Item(vest, 9, 1), Item(vest, 4, 0)]
        gr = GildedRose(items)

        gr.update_quality()

        expect_return = [Item(vest, 0, 1), Item(vest, 8, 0), Item(vest, 3, 0)]
        for actual, expect in zip(gr.get_items_by_name(vest), expect_return):
            assert self.compare(actual, expect)

    def test_Aged_Brie_increase_quality(self):
        vest = "Aged Brie"
        items = [Item(vest, 1, 2), Item(vest, 9, 1), Item(vest, 4, 0)]
        gr = GildedRose(items)

        gr.update_quality()

        expect_return = [Item(vest, 0, 3), Item(vest, 8, 2), Item(vest, 3, 1)]
        for actual, expect in zip(gr.get_items_by_name(vest), expect_return):
            assert self.compare(actual, expect)

    def compare(self, a, b):
        return a.name == b.name and a.sell_in == b.sell_in and a.quality == b.quality
if __name__ == '__main__':
    unittest.main()
