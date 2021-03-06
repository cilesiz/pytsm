# Copyright 2012-2014 VPAC
#
# This file is part of pytsm.
#
# pytsm is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pytsm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pytsm.  If not, see <http://www.gnu.org/licenses/>.

from ..base import TsmCommand


class Command(TsmCommand):
    help = "Display TSM schedule"

    def handle_tsm(self, args, f, d):
        f.output_head("Schedule")

        results = d.execute(
            "SELECT dayofweek, starttime, schedule_name "
            "FROM client_schedules "
            "ORDER BY dayofweek, starttime")

        headers = [
            {"name": "Day", },
            {"name": "Start Time", },
            {"name": "Node", },
        ]

        f.output_results(results, headers)

        d.close()

        f.output_tail()
