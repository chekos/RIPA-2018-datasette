datasette publish heroku datasette/ripa-2018-db.db \
    --branch 0.41 \
    --name ripa-2018-db \
    --install datasette-vega \
    -m datasette/updated_metadata.json \
    --static static:datasette/static/ \
    --template-dir datasette/templates \
    --extra-options="--config default_page_size:50 --config sql_time_limit_ms:30000 --config facet_time_limit_ms:10000"
