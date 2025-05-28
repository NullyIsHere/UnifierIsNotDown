"""
UnifierIsNotDown - UnifierHQ community keeps asking if unifier is down so here is an automated way.
Copyright (C) 2025 ItsAsheer 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import nextcord
from nextcord.ext import commands

class UnifierIsNotDown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        words = message.content.lower().strip().split()

        if len(words) != 3:
            return

        required_words = {"is", "unifier"}
        third_word_options = {"down", "offline"}

        if required_words.issubset(words) and any(w in words for w in third_word_options):
            await message.channel.send("no")

def setup(bot):
    bot.add_cog(UnifierIsNotDown(bot))
