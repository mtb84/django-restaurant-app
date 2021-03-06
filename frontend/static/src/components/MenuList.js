import React from "react";
import menuItems from "../MenuItems";


function MenuList({addToOrder}) {
  
 
    const menuList = menuItems.map((menuItem) => 
       <ul>
          <li className="menu-boxes" key={menuItem.id}>
              <p><strong>{menuItem.name}:</strong> ${menuItem.price}</p>
              <p>--------------</p>  
              <p><em>{menuItem.info}</em></p>
              <p></p>
              <button type="button" className="add-to-order" onClick={() => addToOrder(menuItem)}>Add {menuItem.name} to Order</button>   

          </li>
        </ul>
    
    

    )
    



    
    return (
      <div>
        {menuList}
      </div>
    )
  };

  export default MenuList;