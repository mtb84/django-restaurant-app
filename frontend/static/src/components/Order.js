



function Order({order}) {

    const orderItems = order.map((orderItem, index) =>
     <p key={index}>
        {orderItem.name}: ${orderItem.price}
     </p>
    )

const total = order
  .map(orderItem => orderItem.price)
  .reduce((acc, i) => acc + i, 0);


return(

<div>
  {orderItems}
  <hr className="hr" />
  <div><strong>Total: ${total}</strong></div>
</div>

);


};
export default Order;