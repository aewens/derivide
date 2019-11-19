

import React from 'react'
import universal, { setHasBabelPlugin } from '/root/proto/derivide/client/node_modules/react-universal-component/dist/index.js'

setHasBabelPlugin()

const universalOptions = {
  loading: () => null,
  error: props => {
    console.error(props.error);
    return <div>An error occurred loading this page's template. More information is available in the console.</div>;
  },
  ignoreBabelRename: true
}

const t_0 = universal(import('/root/proto/derivide/client/src/pages/404.js'), universalOptions)
      t_0.template = '/root/proto/derivide/client/src/pages/404.js'
      
const t_1 = universal(import('/root/proto/derivide/client/src/pages/about.js'), universalOptions)
      t_1.template = '/root/proto/derivide/client/src/pages/about.js'
      
const t_2 = universal(import('/root/proto/derivide/client/src/pages/blog.js'), universalOptions)
      t_2.template = '/root/proto/derivide/client/src/pages/blog.js'
      
const t_3 = universal(import('/root/proto/derivide/client/src/pages/index.js'), universalOptions)
      t_3.template = '/root/proto/derivide/client/src/pages/index.js'
      
const t_4 = universal(import('/root/proto/derivide/client/src/containers/Post'), universalOptions)
      t_4.template = '/root/proto/derivide/client/src/containers/Post'
      

// Template Map
export default {
  '/root/proto/derivide/client/src/pages/404.js': t_0,
'/root/proto/derivide/client/src/pages/about.js': t_1,
'/root/proto/derivide/client/src/pages/blog.js': t_2,
'/root/proto/derivide/client/src/pages/index.js': t_3,
'/root/proto/derivide/client/src/containers/Post': t_4
}
// Not Found Template
export const notFoundTemplate = "/root/proto/derivide/client/src/pages/404.js"

