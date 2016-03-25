# Copyright 2014 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sqlalchemy

# (DWang) This version is added to store project and domain info in images,
# and now the 'owner' is specifically the user that created the image.

PROJECT_INDEX = 'project_image_idx'
DOMAIN_INDEX = 'domain_image_idx'


def upgrade(migrate_engine):
    meta = sqlalchemy.MetaData()
    meta.bind = migrate_engine

    images = sqlalchemy.Table('images', meta, autoload=True)

    index = sqlalchemy.Index(PROJECT_INDEX, images.c.project_id)
    index.create(migrate_engine)
    
    index = sqlalchemy.Index(DOMAIN_INDEX, images.c.domain_id)
    index.create(migrate_engine)


def downgrade(migrate_engine):
    meta = sqlalchemy.MetaData()
    meta.bind = migrate_engine

    images = sqlalchemy.Table('images', meta, autoload=True)

    index = sqlalchemy.Index(PROJECT_INDEX, images.c.project_id)
    index.drop(migrate_engine)

    index = sqlalchemy.Index(DOMAIN_INDEX, images.c.domain_id)
    index.drop(migrate_engine)
