// pc0x a command line podcatcher
// Copyright (C) 2010 Bas Bossink <bas.bossink@gmail.com>

// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

#ifndef PODCAST_H_DEFINED
#define PODCAST_H_DEFINED
 
namespace pc0x {
    namespace model {
        class Podcast {
            private:
                int id;
                string feedurl;
                string url;
                string name;
                string genre;
        };
    }
}

#endif 
